from mixer.backend.django import mixer
from vaccination.models import ZipcodeToLatLog


def make_a_zipcode_obj(line):
    try:
        zipcode = mixer.blend(ZipcodeToLatLog, zipcode=line[1], country=line[0])
        zipcode.lat = float(line[-3])
        zipcode.log = float(line[-2])
        zipcode.save()
        print(zipcode.__dict__)
    except Exception as e:
        pass
    print(zipcode.__dict__)


def read_zipcode_file():
    try:
        lineno=0
        with open('/home/rohit/PycharmProjects/immunization/scripts/allCountries.txt') as f:
            line = f.readline()
            data = {}
            while line:
                lineno +=1
                print("line no = {}".format(lineno))
                line = f.readline()
                print()
                line_data = line.split()
                if data.get(line_data[0],False):
                    if len(data[line_data[0]].keys()) >= 10:
                        continue
                    if data[line_data[0]].get(line_data[1],False):
                        if data[line_data[0]][line_data[1]] >= 1:
                            data[ line_data[0] ] [ line_data[1] ] +=1
                            continue
                        else:
                            make_a_zipcode_obj(line_data)
                            data[line_data[0]][line_data[1]] = 1
                    else:
                        make_a_zipcode_obj(line_data)
                        data[line_data[0]][line_data[1]] = 1
                else:
                    make_a_zipcode_obj(line_data)
                    data[line_data[0]] = {line_data[1]:1}
    except Exception as e:
        print(e)


def run():
    try:
        read_zipcode_file()
        print("script run success")
    except Exception as e:
        print(e)
