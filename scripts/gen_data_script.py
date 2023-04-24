from accounts.models import *
from vaccination.models import *
from mixer.backend.django import mixer
from datetime import datetime,timedelta
from django_countries.fields import CountryField
from faker import Faker
import json

fake = Faker()
data = {}
count = 0
vaccine_type = [str(i) for i in range(0,60)]

professions = ['Teacher','Carpainter','Physician','Pharmacist','software developer',
               'Accounttant','Design','Artist','Broker','Surgeon','consultant','Plumber']

doctor_to = datetime.strptime('14-02-1950','%d-%m-%Y')
doctor_from = datetime.strptime('14-02-1990','%d-%m-%Y')

mother_to = datetime.strptime('14-02-1950','%d-%m-%Y')
mother_from = datetime.strptime('14-02-1990','%d-%m-%Y')

father_to = datetime.strptime('14-02-1950','%d-%m-%Y')
father_from = datetime.strptime('14-02-1970','%d-%m-%Y')

child_to = datetime.strptime('14-02-2000','%d-%m-%Y')
child_from = datetime.strptime('14-06-2018','%d-%m-%Y')

def user_data(line,date_to,date_from,gender='male',is_doctor=False,is_patient=False):
    if not gender:
        gender = fake.random_element(('male', 'female'))
    if gender == 'male':
        first_name = fake.first_name_male()
        last_name = fake.last_name_male()
    else:
        first_name = fake.first_name_male()
        last_name = fake.last_name_male()
    if is_doctor and is_patient:
        is_doctor = False
        is_patient = True
    global count
    dob = fake.date_between_dates(date_to,date_from)
    age = (datetime.now().date() - dob).days/365
    email = first_name + last_name + str(count) + '@gmail.com'
    count +=   1
    phone = fake.phone_number()
    pincode = line[1]
    country = CountryField(line[0])
    state= ''
    if len(line) >= 4:
        state = line[3]
    if len(line) >= 6:
        city = line[5]

    address = ''
    for i in line:
        address += i
        address += ' '
    data =  dict(
                first_name = first_name,last_name = last_name,date_of_birth = dob,age = age,
                email = email,phone = phone,pincode = pincode,
                state = state,country = country,   address = address,
                is_patient = is_patient,is_doctor = is_doctor,gender = gender)
    data = change_complex_obj_to_string(data)
    return data

def create_doctor(line):
    doc_data = user_data(line,doctor_to,doctor_from,is_doctor=True)
    rating = fake.random_element([1,2,3,4,5,6])
    experience = fake.random_element([1,2,3,4,5,6,7,8,9,10,11,12,13])
    doc_data.update(dict(rating=rating,experience=experience))
    return doc_data


def create_father(line):
    fat_data = user_data(line, father_to, father_from,gender='male', is_patient=True)
    profession = fake.job()
    fat_data.update(dict(profession=profession))
    return fat_data

def create_mother(line):
    mot_data = user_data(line, mother_to, mother_from, gender='female', is_patient=True)
    profession = fake.job()
    mot_data.update(dict(profession=profession))
    return mot_data

def create_child(line,gender='male'):
    c_data = user_data(line, child_to, child_from, gender=gender,is_patient=True)
    profession = 'Student'
    c_data.update(dict(profession=profession))
    return c_data

def make_vaccine_data(doctor,father,mother,son1,son2,dau):
    mother_dob = datetime.strptime(mother.date_of_birth,'%Y-%m-%d')
    father_dob = datetime.strptime(father.date_of_birth,'%Y-%m-%d')
    doctor_dob = datetime.strptime(doctor.date_of_birth,'%Y-%m-%d')
    son1_dob = datetime.strptime(son1.date_of_birth,'%Y-%m-%d')
    son2_dob = datetime.strptime(son2.date_of_birth,'%Y-%m-%d')
    dau_dob = datetime.strptime(dau.date_of_birth,'%Y-%m-%d')

    max_dob = max(mother_dob,father_dob,doctor_dob)
    father_vacc_date = fake.date_between_dates(max_dob,max_dob + timedelta(days=365 * 10))
    mother_vacc_date = fake.date_between_dates(max_dob,max_dob + timedelta(days=365 * 10))
    son1_vacc_date = fake.date_between_dates(son1_dob,datetime.now().date())
    son2_vacc_date = fake.date_between_dates(son2_dob,datetime.now().date())
    dau_vacc_date = fake.date_between_dates(dau_dob,datetime.now().date())

    get = lambda node_id: Patient.objects.get(pk=node_id)

    mother_vacc_date_str = datetime.strftime(mother_vacc_date, '%Y-%m-%d')
    father_vacc_date_str = datetime.strftime(father_vacc_date, '%Y-%m-%d')
    son1_vacc_date_str = datetime.strftime(son1_vacc_date, '%Y-%m-%d')
    son2_vacc_date_str = datetime.strftime(son1_vacc_date, '%Y-%m-%d')
    dau_vacc_date_str = datetime.strftime(dau_vacc_date, '%Y-%m-%d')

    Patient.objects.filter(pk=mother.pk).update(**{'last_visit':mother_vacc_date_str})
    Patient.objects.filter(pk=father.pk).update(**{'last_visit':father_vacc_date_str})
    Patient.objects.filter(pk=son1.pk).update(**{'last_visit':son1_vacc_date_str})
    Patient.objects.filter(pk=son2.pk).update(**{'last_visit':son2_vacc_date_str})
    Patient.objects.filter(pk=dau.pk).update(**{'last_visit':dau_vacc_date_str})

    father_vacc = {'name': 'Vaccine ' + fake.random_element(vaccine_type), 'patient': father, 'doctor': doctor,
                   'date_of_vaccination': father_vacc_date_str}
    mother_vacc = {'name': 'Vaccine ' + fake.random_element(vaccine_type), 'patient': mother, 'doctor': doctor,
                   'date_of_vaccination': mother_vacc_date_str}
    son1_vacc = {'name': 'Vaccine ' + fake.random_element(vaccine_type), 'patient': son1, 'doctor': doctor,
                   'date_of_vaccination': son1_vacc_date_str}
    son2_vacc = {'name': 'Vaccine ' + fake.random_element(vaccine_type), 'patient': son2, 'doctor': doctor,
                   'date_of_vaccination': son2_vacc_date_str}
    dau_vacc = {'name': 'Vaccine ' + fake.random_element(vaccine_type), 'patient': dau, 'doctor': doctor,
                   'date_of_vaccination': dau_vacc_date_str}

    fv = VaccinationChart.objects.create(**father_vacc)
    print("father vaccine created : {}".format(fv.__dict__))

    mv = VaccinationChart.objects.create(**mother_vacc)
    print("mother vaccine created : {}".format(mv.__dict__))

    s1 = VaccinationChart.objects.create(**son1_vacc)
    print("son1 vaccine created : {}".format(s1.__dict__))

    s1 = VaccinationChart.objects.create(**son2_vacc)
    print("son2 vaccine created : {}".format(s1.__dict__))

    s1 = VaccinationChart.objects.create(**dau_vacc)
    print("daughter vaccine created : {}".format(s1.__dict__))



def create_object(line):
    doctor_data = create_doctor(line)
    doctor = Doctor.objects.create(**doctor_data)
    print("Doctor created : {}".format(Doctor.email))
    mother_data = create_mother(line)
    father_data = create_father(line)
    son1_data = create_child(line)
    son2_data = create_child(line)
    dau_data = create_child(line,gender='female')
    father,mother,son1,son2,dau = make_family(father_data,mother_data,son1_data,son2_data,dau_data)
    make_vaccine_data(doctor,father,mother,son1,son2,dau)

def change_complex_obj_to_string(data):
    data.update({'date_of_birth':datetime.strftime(data['date_of_birth'], '%Y-%m-%d'),
                 'country':data['country']._verbose_name})
    return data

def make_family(father_data,mother_data,son1_data,son2_data,dau_data):
    get = lambda node_id: Patient.objects.get(pk=node_id)
    father = Patient.add_root(**father_data)
    print("father created : {}".format(father.email))
    # Patient.objects.filter(pk=father.pk).update(**father_data)
    son1 = get(father.pk).add_child(**son1_data)
    print("son1 created : {}".format(son1.email))
    son2 = get(son1.pk).add_sibling(**son2_data)
    print("son2 created : {}".format(son2.email))
    dau = get(son2.pk).add_sibling(**dau_data)
    print("daughter created : {}".format(dau.email))
    mother = get(dau.pk).add_sibling(pos='first-sibling',**mother_data)
    print("mother created : {}".format(mother.email))
    return [father,mother,son1,son2,dau]


def read_zipcode_file():

    with open('/home/rohit/PycharmProjects/immunization/scripts/allCountries.txt') as f:
        line = f.readline()
        data = {}
        lineno = 0
        while line:
            line = f.readline()
            lineno += 1
            print("line no {}".format(lineno))
            line_data = line.split()
            if len(line_data) < 2:
                continue
            print("line is {}".format(line_data))
            print("data is  {}".format(data))
            if data.get(line_data[0],False):
                if len(data[line_data[0]].keys()) >= 10:
                    print("we are continuing keys at most 10 zipcoes from a country-------------->\n\n")
                    continue
                if data[line_data[0]].get(line_data[1],False):
                    print("on country {} zipcodes {}".\
                          format(line_data[0],len(data[line_data[0]].keys()) ))
                    if data[line_data[0]][line_data[1]] >= 1:
                        print("we are continuing --------at most one family from a zipcode------>\n\n")
                        data[ line_data[0] ] [ line_data[1] ] +=1
                        continue
                    else:
                        data[line_data[0]][line_data[1]] = 1
                else:
                    data[line_data[0]][line_data[1]] = 1
            else:
                data[line_data[0]] = {line_data[1]:1}

            create_object(line_data)
    with open('zipcodes.json') as f:
        f.write(json.dumps(data))


def run():
    try:
        read_zipcode_file()
        print("script run success")
    except Exception as e:
        print(e)