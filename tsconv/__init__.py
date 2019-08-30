import enum
import time
import datetime
import pytz
import sys

SHANGHAI_TZ = pytz.timezone('Asia/Shanghai')

MIN_DATE = datetime.datetime(year=2000, month=1, day=1)
MAX_DATE = MIN_DATE + datetime.timedelta(days=100*365)
MIN_TS = MIN_DATE.timestamp()
MAX_TS = MAX_DATE.timestamp()


class UnitPerSec(enum.IntEnum):
    SEC = 1
    MILI_SEC = int(1e3)
    MICRO_SEC = int(1e6)
    NANO_SEC = int(1e9)


def is_resonable(ts: float):
    return MIN_TS <= ts <= MAX_TS


def check_interval():
    MAX_TS  < MIN_TS * UnitPerSec.MILI_SEC


def guess_ts_unit(ts: float):
  for unit_per_sec in UnitPerSec:
    if is_reasonable(ts/unit_per_sec.value):
      return unit_per_sec
  else:
    raise ValueError('Timestamp value not in reasonable range!')


def ts_to_datetime(ts, tz):
  unit_per_sec = guess_ts_unit(ts)
  ts = ts / unit_per_sec.value
  return datetime.datetime.fromtimestamp(ts, tz)


def print_usage():
  dt = datetime.datetime.now()
  tm = dt.timestamp()
  print(dt)
  print(tm)
  print(int(tm*(10**3)))
  print(int(tm*(10**6)))
  print(int(tm*(10**9)))


def main(argv=None):
  argv == sys.argv
  if len(argv) == 2:
    timestamp = float(argv[1])
    dt = ts_to_datetime(timestamp, SHANGHAI_TZ)
    print(dt)

if __name__ == "__main__":
  sys.exit(main(sys.argv))
