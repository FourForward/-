"""
百度坐标系已经失效

火星坐标系为高德地图坐标系
"""
import math

PI = math.pi
AXIS = 6378245.0
OFFSET = 0.00669342162296594323
X_PI = PI * 3000.0 / 180.0


# GCJ - 02 = > BD09     火星坐标系 = > 百度坐标系
def gcj2BD09(glat, glon):
    x = glon
    y = glat
    latlon = []
    z = math.sqrt(x * x + y * y) + 0.00002 * math.sin(y * X_PI)
    theta = math.atan2(y, x) + 0.000003 * math.cos(x * X_PI)
    latlon.append(z * math.sin(theta) + 0.006)
    latlon.append(z * math.cos(theta) + 0.0065)
    return latlon


# BD09=>GCJ-02      百度坐标系=>火星坐标系
def bd092GCJ(glat, glon):
    x = glon - 0.0065
    y = glat - 0.006
    latlon = []
    z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * X_PI)
    theta = math.atan2(y, x) - 0.000003 * math.cos(x * X_PI)
    latlon.append(z * math.sin(theta))
    latlon.append(z * math.cos(theta))
    return latlon


# BD09=>WGS84   百度坐标系=>地球坐标系
def bd092WGS(glat, glon):
    latlon = bd092GCJ(glat, glon)
    return gcj2WGS(latlon[0], latlon[1])


# WGS84=》BD09   地球坐标系=>百度坐标系
def wgs2BD09(wgLat, wgLon):
    latlon = wgs2GCJ(wgLat, wgLon)
    return gcj2BD09(latlon[0], latlon[1])


# WGS84=》GCJ02   地球坐标系=>火星坐标系
def wgs2GCJ(wgLat, wgLon):
    latlon = []
    if outOfChina(wgLat, wgLon):
        latlon.append(wgLat)
        latlon.append(wgLon)
        return latlon
    deltaD = delta(wgLat, wgLon)
    latlon.append(wgLat + deltaD[0])
    latlon.append(wgLon + deltaD[1])
    return latlon


# GCJ02=>WGS84   火星坐标系=>地球坐标系(粗略)
def gcj2WGS(glat, glon):
    latlon = []
    if outOfChina(glat, glon):
        latlon.append(glat)
        latlon.append(glon)
        return latlon
    deltaD = delta(glat, glon)
    latlon.append(glat - deltaD[0])
    latlon.append(glon - deltaD[1])
    return latlon


# GCJ02=>WGS84   火星坐标系=>地球坐标系（精确）
def gcj2WGSExactly(gcjLat, gcjLon):
    initDelta = 0.01
    threshold = 0.000000001
    dLat = initDelta, dLon = initDelta
    mLat = gcjLat - dLat
    mLon = gcjLon - dLon
    pLat = gcjLat + dLat
    pLon = gcjLon + dLon
    wgsLat, wgsLon, i = 0, 0, 0
    while True:
        wgsLat = (mLat + pLat) / 2
        wgsLon = (mLon + pLon) / 2
        tmp = wgs2GCJ(wgsLat, wgsLon)
        dLat = tmp[0] - gcjLat
        dLon = tmp[1] - gcjLon
        if (abs(dLat) < threshold) and (abs(dLon) < threshold): break
        if dLat > 0:
            pLat = wgsLat
        else:
            mLat = wgsLat
        if dLon > 0:
            pLon = wgsLon
        else:
            mLon = wgsLon
        i += 1
        if i > 10000: break
    latlon = []
    latlon.append(wgsLat)
    latlon.append(wgsLon)
    return latlon


# 两点距离
def distance(latA, logA, latB, logB):
    earthR = 6371000
    x = math.cos(latA * math.PI / 180) * math.cos(latB * math.PI / 180) * math.cos((logA - logB) * math.PI / 180)
    y = math.sin(latA * math.PI / 180) * math.sin(latB * math.PI / 180)
    s = x + y
    if s > 1:
        s = 1
    if s < -1:
        s = -1
    alpha = math.acos(s)
    distance = alpha * earthR
    return distance


def delta(wgLat, wgLon):
    latlng = []
    dLat = transformLat(wgLon - 105.0, wgLat - 35.0)
    dLon = transformLon(wgLon - 105.0, wgLat - 35.0)
    radLat = wgLat / 180.0 * PI
    magic = math.sin(radLat)
    magic = 1 - OFFSET * magic * magic
    sqrtMagic = math.sqrt(magic)
    dLat = (dLat * 180.0) / ((AXIS * (1 - OFFSET)) / (magic * sqrtMagic) * PI)
    dLon = (dLon * 180.0) / (AXIS / sqrtMagic * math.cos(radLat) * PI)
    latlng.append(dLat)
    latlng.append(dLon)
    return latlng


def outOfChina(lat, lon):
    if lon < 72.004 or lon > 137.8347:
        return True
    if lat < 0.8293 or lat > 55.8271:
        return True
    return False


def transformLat(x, y):
    ret = -100.0 + 2.0 * x + 3.0 * y + 0.2 * y * y + 0.1 * x * y + 0.2 * math.sqrt(abs(x))
    ret += (20.0 * math.sin(6.0 * x * PI) + 20.0 * math.sin(2.0 * x * PI)) * 2.0 / 3.0
    ret += (20.0 * math.sin(y * PI) + 40.0 * math.sin(y / 3.0 * PI)) * 2.0 / 3.0
    ret += (160.0 * math.sin(y / 12.0 * PI) + 320 * math.sin(y * PI / 30.0)) * 2.0 / 3.0
    return ret


def transformLon(x, y):
    ret = 300.0 + x + 2.0 * y + 0.1 * x * x + 0.1 * x * y + 0.1 * math.sqrt(abs(x))
    ret += (20.0 * math.sin(6.0 * x * PI) + 20.0 * math.sin(2.0 * x * PI)) * 2.0 / 3.0
    ret += (20.0 * math.sin(x * PI) + 40.0 * math.sin(x / 3.0 * PI)) * 2.0 / 3.0
    ret += (150.0 * math.sin(x / 12.0 * PI) + 300.0 * math.sin(x / 30.0 * PI)) * 2.0 / 3.0
    return ret


if __name__ == '__main__':
    print(wgs2GCJ(30.6741378, 104.0105694))
