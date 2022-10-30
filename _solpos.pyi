from typing import TypedDict

class D(TypedDict):
    year: int
    month: int
    day: int
    hour: int
    minute: int
    second: float
    timezone: float
    interval: int
    latitude: float
    longitude: float
    amass: float
    ampress: float
    aspect: float
    azim: float
    cosinc: float
    coszen: float
    dayang: float
    declin: float
    eclong: float
    ecobli: float
    ectime: float
    elevetr: float
    elevref: float
    eqntim: float
    erv: float
    etr: float
    etrn: float
    etrtilt: float
    gmst: float
    hrang: float
    julday: float
    lmst: float
    mnanom: float
    mnlong: float
    rascen: float
    press: float
    prime: float
    sbcf: float
    sbwid: float
    sbrad: float
    sbsky: float
    solcon: float
    ssha: float
    sretr: float
    ssetr: float
    temp: float
    tilt: float
    tst: float
    tstfix: float
    unprime: float
    utime: float
    zenetr: float
    zenref: float

def _solpos(
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        second: int,
        timezone: float,
        latitude: float,
        longitude: float,
        interval: int,
        aspect: float,
        press: float,
        sbwid: float,
        sbrad: float,
        sbsky: float,
        solcon: float,
        temp: float,
        tilt: float,
) -> D: ...
