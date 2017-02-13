# Copyright 2017 Gordon D. Thompson
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import base64
import gzip
import os
import shutil
import tempfile

"""Module to create a new (empty) Access database."""


def create(filespec):
    """Create a new (empty) Access database.

    Note that no effort is made to avoid overwriting an existing file.

    :type filespec: str
    """
    if filespec.lower().endswith(".accdb"):
        _unpack_and_save(_accdb_gz_b64, filespec)
    else:
        _unpack_and_save(_mdb_gz_b64, filespec)


def _unpack_and_save(packed_data, filespec):
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file_spec = tmp_file.name
        tmp_file.write(base64.b64decode(packed_data))
    with gzip.open(tmp_file_spec, 'rb') as f_in, open(filespec, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
    os.remove(tmp_file_spec)


_mdb_gz_b64 = """\
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
"""

_accdb_gz_b64 = """\
H4sICBKnn1gC/25ldzIwMDcuYWNjZGIA7d0LbBzHecDx2bu994ukFMl60KTeOsd2JNly0jRAKImm
LUIkTZG0wiSVROpIieFLlWjVatKYlmQ0doLGeSFukcK1nUBwgQJNmrRImkJJGkcI8kTRFkkRx2mt
Fkhrt0Wbh522un4zu3uvvaMoifDR1P93urvZmdmZ3b09Ut/O3FFZSvXNDE3lhk7kWnftubu1fbcK
KKW+MBUcPhz72sBPnz16ou3t6lPvf/Lx/CN/sP250196eduXX/j2Hx754aW/frLjfx77cveT737p
ze0vfupXL7y69V/ijY8d7rrjvXe99HcvfHaqb9mev49+9o7bvnH6XR9set8tz/zkfb8fbXni/9pC
zSve+fy50UOfeOX7j2585Og3Wra0/82/f2/k5XzkYsdTD65IvvzT24b/tj+s1J23b1MAAAAAgIVh
WYrbDXyzrFzGcs+FgPrLzKkM7wkAAAAAABal/81fs4D144RuYrWt1GBYqSbvulBFF32NKqEazdQA
fVdS1Qo7RU0l1bx0UrcVU0FJxuzSKqYgatooL4jqAtv0qwuWmcy4VDUFoYqCJimwdUGk0JRTsFra
iOuCuCTK+7hsmTUcxTV0rwldkJLGKrfKFDRIY1ULMrKLVQvSsnmVBWarAoXOi1sV0wXhwg7uKN9c
q2JzbW9zk/o1qOjDNJWQo1XZR1AXBCsOon4Z0mqPmlZTchtRR9SM7Gu7GpLnITUs95OSu9zNGZGa
J+TRSRdzB9RxlXPTcdWhJiR9VNZcIelps8aYLE+pbsmflCVb7ZX6ttqnTknv+vFu9aCsfULKG8xy
l6yXUw9ISyOylzrnPimdln6ihVbiqkf9ltnqE7LWfZKre5qSdnTrK9R+qaXTU2pU1txn9vGouqki
v08dM9s4Iy33q9PSw4g6G9EH3QooK59XVf81mPPO8bB5PGsWa64g/xrNaV+6jvfimhdYvxXNq2tb
XllBscw9AfQe3uTbZ+/IxJSt3zDO20y/6ubUjur3ozmX0/rENSdvUpeYszWuTxvnnNL7Ftad8mMV
AAAAWGoC1rNp/dxjOVHHzlrxvw7N7WLAIoGvFSuP+W0nwLV84apVLfjU7dSMx2PlkW8xJA6rXRKG
dkn402GCuGMmABxzA1YdMDZIYDis3uOGszowCkuYt1fC1SsHaYGYMqG+9gF1pUDM3xNBEwAAAABg
0cb//5bSz6lAebDrxf8h994XlbA8Woz/E/KcqGiq+nC15Yz5h6pMBgg6I9922RohFfCG9ssLIt7Q
fvFSgtPUO95y2Yo70wcq5xXMMeYfqzUe36R2STw/Y64rDKsH3OFuPUh93Ay4npTbmBlQjhaGuysH
suOF4djtJekdVa4Z6IHsE/Ksr2O4VyjmGH22E3qQVqwtHUaucoXCvA7rfb3590wOt7QZTDDkCwAA
AABLPP7/loknbwtWj/+9iFLi/5DEuzqGD5rrBVIlNb8uas4LcOe3W77Q3K4+W90N/0MVUf4rsUL4
b/mC+Xj5lYSKgnDFRYlLbW6BqrguELcuW2mJoo9I3D8hkfOkRP9xiftPSBytZx+k5bG0rEGdVL9t
ptaX55TG4xtNzn5ZGjXRv57KfUQec2Xr1a5V2tbaQq0JMxXfuT5xUh2T1PHizIeL3oWE2Xz+0/n8
tnx+fz7/Sj5/KZDS08DFFqXOmD3W69h6Hadet1ltpPRaRDClJ5E7iuuE9TqXyi9bfK54/SKl500o
1XZhpPtM4fpFlWnwhbLCJ06qlFW57mEWr+ZYz/8ocn0EAAAAwOuaZf3Mm/Euoa7+/r/tmZfS59PD
6eb0D1IfS3WnYqmvJx9KvjX588SfJsYTmxMcMwAAANwg/1degDZmOYwAtED9G7GteLJmC61Ktekf
e3rE1vb6kkyd6yRMUav3c81y61hmscGphnp66MP6oadzsnNf53jvuH6FGi0nc6z3YOfkYG54/MDg
qFMQcAqk7kG3qlnfeujw+Knxzi43L1TM68odHj3Y+0BX7uD04WGnNOornTw12vvGYOfkZGfXgcO9
w5OmWmONaj29XYOHOw+aOpkadQamB3tMhXSNCoO9vb09uWnZC1MtNUe18cHhAbdaska1g7nhAVMh
UaPC+IHcmLNX8Ro1JiVhKjTUqDA9PD44MNzbs+/UpLMxsWLF3L539XZNOkfXLmYfm+4dG3RfknAx
2/+qRnRhwBT27DM5Qd4XAAAAwI3Itt6fqhX/B+xoQ2vbrLJKEhyx11n8P2uuyEjgOGs+uSHR+6y5
mCMx46z5ageJD2fNxxwkdJfEShN8SmKViWclscaEvpJoNkGyJFpMUC2JdSYIl8QGE65LYpMJcmfN
BwncIN+7jBDwLj0EzaWGx832EYsCAAAAwGvDspq9z3BLXObM/+eoAAAAAABgLNg4eL0/AmBbe5K1
hmCrjf/PM8EZski44//ZQmKFl9jszgjIJrzEOndqQDbpJdZ7iQ3uZIFsykts9BKb3OkDWctLrPQS
W9wJBdmAl7jJS2x1pxhkg15ilZfIupMOsraXWO0lbnGnIWRDXmKNl3ijOzEhG/YSa73Ere5UhWzE
SzR7idvcyQvZqJe42Uvc7k5nyMa8RIuXeJM7wSEb9xKtXmKbO+Uhm/YSGS+x3UvscGdDZJvc2RDZ
Bi/R6CXu8BJ3uhMlssu8xHIv8QZObwAAAABXwbI+nPbSoZLv/+PIAAAAAADqpoFDsNBsqzXNh/oB
AAAAAFjaGP8HAAAAACzCaHUB2phdiA1pWypHVI//hzixAAAAAABY0oj/AQAAAAAg/gcAAAAAAK9/
lhWPeX8+sEl9IZPLJDJfSY+n16YvpkZTodTjyWzy64m+xD/FfyfeFP+T2NtiHDMAAHDjatR/8VV/
JjVjqV+8+8CZu1681OY9KxWc7VJ96rQ6qfaoaTWpjqsJNaIeVP2Sd1xSh9QuNSO3IXVEHZPyETUl
S/1Vb60qoS7oDjf5OvzlVXTYb5Zn1L1Vb4VONlxXJ+3yeESNSdmQlHVXvRW6WnddXd2jBtRe6fAK
+9NS6OTC/U7jX7l//p3sVXebW7uUP6CGTfkVXqXmBemwTw7ilDo6nw7XXFeH+yRfd3SFw7jqujrp
k5N8Wp2Qs6+z6q3Qzcrr6mZA9uSkHLij8jyicmq3lMxI6h1Vb4VOm3ydXih0qmp0qpcm5JSYNF22
V70VOgjNq4P90vCEvG9mZA+mTbPHJHVcnp/+jWrN7zYd5HUH9rw66JXtHZFXYUwedaNvUf7bXcVG
g4VGH73Pacx7Lm10lxyKu01zO5T/tq3YXGBezfXIm+w95ofIzHy2UTRIw5nAnI22S6PPHLpd+W+3
lu1uRlbKBKs2NdeL8zblv721bMfnaLjdNDokWzgkjTkvzJ3Kf9tRbNCas8F+09iE29ScOx2w2lP6
EH5eNnEwXHJdoOJ3XXdIskLmhNB3tUyqLJvfr8l4sd2Ybf4wvGn/smXrAtt0pQtWmoKk5JgCq1Dg
9eMWBCsKol5BoKJAstXysrdptxwY/Zu2qeKtrH+JbK7xM6X0dNT11pt6U7I8IuUz0rL+PVc85LrO
CtXhnirl+WcjZofzeVXrX0A2fbm7vx80j3qd4JzrBGUd72/BP1ZYJzDnOrass6JsHeeYu698XphD
aBfK9Js3UKOsoFhmmtkqe51zf1TOfcTWujWrH7e4W6rTTgcAAAAAgKvD9/8DAAAAABaftoVopHUh
GmlYIkdUf/6/iRMLAAAAAIAljfgfAAAAAADifwAAAAAA8PoXsD6qv0hQjaorfP+fVZ55kyzJPVD+
3X7Bwtpxdb/5ljf9dZN8YxsAAAAAAPVlWblM4VqA+f4/jgkAAAAAAEvNtY7/r5YluQerj/8HGP8H
AAAAAGARYfwfAAAAAICl71rH/9fKktzt6uP/NuP/AAAAAAAsIoz/AwAAAACw9F3r+P/NsiT3MOP/
AAAAAAAsfoz/AwAAAACw9F3r+H+rLMk9Un38P8r4PwAAAAAAiwjj/wAAAAAALH3XOv6/Xpbknqk+
/t/A+D8AAAAAAIsI4/8AAAAAACx9VzH+b5VmbpQqcm8ortOkW3PTMcb/AQAAAABYRBj/BwAAAABg
6bvW8f/NUkXu8fLP/3vj/5ctxv8BAAAAAFg8GP8HAAAAAGDpC1ifTOvnIesK4/9hZauS8q1SRe4J
vU7QfO+/Gf9v8MptXRCSddw/DGAKorJsZgw4UwlK17hsRXWBXbGGXsesETBzC8rXSFZMPih03qA6
1JiaUCOqXQ2pGbk3FXI65HFIHVUnS2p1S86kPK8u5PTLs87pM2tPquMltfvVaVkeUelCzoDar/bJ
QbDliIS2msMqj0G5M/UBAAAAALAoWNa9aS8dNuP/2zMvpc+nh9McGwAAAAAAlk78/3M76KZ3qpcz
/5C5mPl85qnM72XemzmWGcjszrwpszYTy/wi/WL6++m/Sv9x+pPpc+nfTP8qdTaVTH0ieXPyfGJb
4ovx3fFvxfpjz0dHo/8R+VFkJLI/8vbIrZFVkXDkv8M/CX8n/KXw+fDHww+H4+FfhmZDkyGOPIAb
iq0nSmXy+Yx6+lBSxZWlMsWspx4Z2dnymS92HRhv+Ujfd1994tQfXXj47I83j+w80/GPj/+utX76
sVv+859Hf+3iz37U8YHuricmAo8++2d7P7TzznN/MfXDYz+459Sh5869+Oqvf/WOI/e8+UNrUs+r
xplvbm3Z86/rzpzf+OefO9d68bncxW3/de9xr1tLd3u5bEu8rNd4S7bIkVkud29LIrba5M/a4M9a
589q8Wc1+7PW+LNW+bNW+rOa/FkBf1aoVlb4NT20EWcyXcWW2PXZEuf/GK95t1vqs7eb6tPthvp0
u64+3bbUp9vm+nS7pj7drqpPtyvr021TfboN1Kdb0ZCuV7dlv5S8LXmm7PdqRpVn6f8pWf6sy1Lx
6XeW/S+mopblr+UEoOnSWrb7K6q8+cqsLf6sTf6sDf6sdf6sFn9Wsz9rjT9rlT9rpT+ryZ8VqMz6
f/xJCu4AoAIA
"""
