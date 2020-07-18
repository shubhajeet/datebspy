# DateBS

A python library that assists you in converting date from BS to AD and vice versa.

# Installation

```bash
pip install datebs
```

## usage

### Commandline

convert the date 2020-07-01 into BS
```bash
python -m datebs BS --date 2020-07-01
```

### using from python
```python
from datebs import DateBS
import argparse
import datetime

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="python -m datebs",description='Convert date from BS to AD and vice-versa')
    parser.add_argument('calendar',type=str, help="calendar system in which date is to be displayed [AD|BS]")
    parser.add_argument('--date',type=str, help="date opporsite to the calendar system")
    args = parser.parse_args()
    if (args.calendar == "BS"):
        if args.date:
            dateBS = DateBS.from_AD(datetime.datetime.strptime(args.date, "%Y-%m-%d"))
        else:
            dateBS = DateBS.from_AD(datetime.datetime.now())
        print(dateBS)
    else:
        if args.date:
            dateBS = DateBS.from_string(args.date)
            print(dateBS.to_AD())
        else:
            print(datetime.datetime.now())
```

### From LibreOffice calc
Use above formula to convert the date from one string format to another
- DateToBS(datestring)
- DateToAD(datestring)
