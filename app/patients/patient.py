from dataclasses import dataclass
from language_strings.language_string import LanguageString
from client_object import ClientObject
from datetime import datetime, date
from util import identity, parse_client_date, parse_client_timestamp


@dataclass
class Patient(ClientObject):
    id: str
    given_name: LanguageString
    surname: LanguageString
    date_of_birth: date
    sex: str
    country: LanguageString
    hometown: LanguageString
    phone: str
    medical_record_num: str
    attention_datetime: datetime
    attending_resources: str
    origin: str
    age: str
    email: str
    educational_status: str
    religion: str
    marital_status: str
    occupation: str
    mother_name: str
    father_name: str
    delivery_place: str
    delivery_datetime: datetime
    gestational_age: str
    delivery_care: str
    delivery_via: str
    presentation: str
    birthing_events: str
    edited_at: datetime

    def client_insert_values(self):
        return [self.id,
                self.format_string(self.given_name),
                self.format_string(self.surname),
                self.format_date(self.date_of_birth),
                self.sex,
                self.format_string(self.country),
                self.format_string(self.hometown),
                self.phone,
                self.medical_record_num, 
                self.format_ts(self.attention_datetime),
                self.attending_resources, 
                self.origin, 
                self.age, 
                self.email, 
                self.educational_status, 
                self.religion, 
                self.marital_status, 
                self.occupation, 
                self.mother_name, 
                self.father_name, 
                self.delivery_place, 
                self.format_ts(self.delivery_datetime),
                self.gestational_age, 
                self.delivery_care, 
                self.delivery_via, 
                self.presentation, 
                self.birthing_events, 
                self.format_ts(self.edited_at)]

    @classmethod
    def client_insert_sql(cls):
        return """INSERT INTO patients (id, given_name, surname, date_of_birth, sex, country, hometown, phone, medical_record_num, attention_datetime, attending_resources, origin, age, email, educational_status, religion, marital_status, occupation, mother_name, father_name, delivery_place, delivery_datetime, gestational_age, delivery_care, delivery_via, presentation, birthing_events, edited_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""

    def client_update_values(self):
        return [self.format_string(self.given_name),
                self.format_string(self.surname),
                self.format_date(self.date_of_birth),
                self.sex,
                self.format_string(self.country),
                self.format_string(self.hometown),
                self.phone,
                self.medical_record_num, 
                self.format_ts(self.attention_datetime),
                self.attending_resources, 
                self.origin, 
                self.age, 
                self.email, 
                self.educational_status, 
                self.religion, 
                self.marital_status, 
                self.occupation, 
                self.mother_name, 
                self.father_name, 
                self.delivery_place, 
                self.format_ts(self.delivery_datetime),
                self.gestational_age, 
                self.delivery_care, 
                self.delivery_via, 
                self.presentation, 
                self.birthing_events, 
                self.format_ts(self.edited_at),
                self.id]

    @classmethod
    def client_update_sql(cls):
        return """UPDATE patients SET given_name = ?, surname = ?, date_of_birth = ?, sex = ?, country = ?, hometown = ?, phone = ?, medical_record_num = ? , attention_datetime = ? , attending_resources = ? , origin = ? , age = ? , email = ? , educational_status = ? , religion = ? , marital_status = ? , occupation = ? , mother_name = ? , father_name = ? , delivery_place = ? , delivery_datetime = ? , gestational_age = ? , delivery_care = ? , delivery_via = ? , presentation = ? , birthing_events = ? , edited_at = ? WHERE id = ?"""
            

    def server_insert_values(self):
        return [self.id,
                self.format_string(self.given_name),
                self.format_string(self.surname),
                self.date_of_birth,
                self.sex,
                self.format_string(self.country),
                self.format_string(self.hometown),
                self.phone,
                self.medical_record_num, 
                self.format_ts(self.attention_datetime),
                self.attending_resources, 
                self.origin, 
                self.age, 
                self.email, 
                self.educational_status, 
                self.religion, 
                self.marital_status, 
                self.occupation, 
                self.mother_name, 
                self.father_name, 
                self.delivery_place, 
                self.format_ts(self.delivery_datetime),
                self.gestational_age, 
                self.delivery_care, 
                self.delivery_via, 
                self.presentation, 
                self.birthing_events, 
                self.edited_at]

    @classmethod
    def server_insert_sql(cls):
        return """INSERT INTO patients (id, given_name, surname, date_of_birth, sex, country, hometown, phone, medical_record_num, attention_datetime, attending_resources, origin, age, email, educational_status, religion, marital_status, occupation, mother_name, father_name, delivery_place, delivery_datetime, gestational_age, delivery_care, delivery_via, presentation, birthing_events, edited_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    def server_update_values(self):
        return [self.format_string(self.given_name),
                self.format_string(self.surname),
                self.date_of_birth,
                self.sex,
                self.format_string(self.country),
                self.format_string(self.hometown),
                self.phone,
                self.medical_record_num, 
                self.format_ts(self.attention_datetime),
                self.attending_resources, 
                self.origin, 
                self.age, 
                self.email, 
                self.educational_status, 
                self.religion, 
                self.marital_status, 
                self.occupation, 
                self.mother_name, 
                self.father_name, 
                self.delivery_place, 
                self.format_ts(self.delivery_datetime),
                self.gestational_age, 
                self.delivery_care, 
                self.delivery_via, 
                self.presentation, 
                self.birthing_events, 
                self.edited_at,
                self.id]

    @classmethod
    def server_update_sql(cls):
        return """UPDATE patients SET given_name = %s, surname = %s, date_of_birth = %s, sex = %s, country = %s, hometown = %s, phone = %s, medical_record_num = %s , attention_datetime = %s , attending_resources = %s , origin = %s , age = %s , email = %s , educational_status = %s , religion = %s , marital_status = %s , occupation = %s , mother_name = %s , father_name = %s , delivery_place = %s , delivery_datetime = %s , gestational_age = %s , delivery_care = %s , delivery_via = %s , presentation = %s , birthing_events = %s , edited_at = %s WHERE id = %s"""


    @classmethod
    def db_columns_from_server(cls):
        return [('id', lambda s: s.replace('-', '')),
                ('given_name', cls.make_language_string),
                ('surname', cls.make_language_string),
                ('date_of_birth', identity),
                ('sex', identity),
                ('country', cls.make_language_string),
                ('hometown', cls.make_language_string),
                ('phone', identity),
                ('medical_record_num', identity)
                ('attention_datetime', identity)
                ('attending_resources', identity)
                ('origin', identity)
                ('age', identity)
                ('email', identity)
                ('educational_status', identity)
                ('religion', identity)
                ('marital_status', identity)
                ('occupation', identity)
                ('mother_name', identity)
                ('father_name', identity)
                ('delivery_place', identity)
                ('delivery_datetime', identity)
                ('gestational_age', identity)
                ('delivery_care', identity)
                ('delivery_via', identity)
                ('presentation', identity)
                ('birthing_events', identity)
                ('edited_at', identity)]

    @classmethod
    def db_columns_from_client(cls):
        return [('id', identity),
                ('given_name', cls.make_language_string),
                ('surname', cls.make_language_string),
                ('date_of_birth', parse_client_date),
                ('sex', identity),
                ('country', cls.make_language_string),
                ('hometown', cls.make_language_string),
                ('phone', identity),
                ('medical_record_num', identity)
                ('attention_datetime', parse_client_timestamp),
                ('attending_resources', identity)
                ('origin', identity)
                ('age', identity)
                ('email', identity)
                ('educational_status', identity)
                ('religion', identity)
                ('marital_status', identity)
                ('occupation', identity)
                ('mother_name', identity)
                ('father_name', identity)
                ('delivery_place', identity)
                ('delivery_datetime', parse_client_timestamp),
                ('gestational_age', identity)
                ('delivery_care', identity)
                ('delivery_via', identity)
                ('presentation', identity)
                ('birthing_events', identity)
                ('edited_at', parse_client_timestamp)]

    @classmethod
    def table_name(cls):
        return "patients"

    @classmethod
    def from_db_row(cls, db_row):
        id, given_name, surname, date_of_birth, sex, country, hometown, phone, medical_record_num, attention_datetime, attending_resources, origin, age, email, educational_status, religion, marital_status, occupation, mother_name, father_name, delivery_place, delivery_datetime, gestational_age, delivery_care, delivery_via, presentation, birthing_events, edited_at = db_row
        return cls(id, LanguageString.from_id(given_name), LanguageString.from_id(surname), date_of_birth, sex, LanguageString.from_id(country), LanguageString.from_id(hometown), phone, medical_record_num, attention_datetime, attending_resources, origin, age, email, educational_status, religion, marital_status, occupation, mother_name, father_name, delivery_place, delivery_datetime, gestational_age, delivery_care, delivery_via, presentation, birthing_events, edited_at)    

    def to_dict(self):
        return {
            'id': self.id,
            'given_name': self.given_name.to_dict() if self.given_name is not None else None,
            'surname': self.surname.to_dict() if self.surname is not None else None,
            'date_of_birth': self.date_of_birth,
            'sex': self.sex,
            'country': self.country.to_dict() if self.country is not None else None,
            'hometown': self.hometown.to_dict() if self.hometown is not None else None,
            'phone': self.phone,
            'medical_record_num': self.medical_record_num, 
            'attention_datetime': self.attention_datetime, 
            'attending_resources': self.attending_resources, 
            'origin': self.origin, 
            'age': self.age, 
            'email': self.email, 
            'educational_status': self.educational_status, 
            'religion': self.religion, 
            'marital_status': self.marital_status, 
            'occupation': self.occupation, 
            'mother_name': self.mother_name, 
            'father_name': self.father_name, 
            'delivery_place': self.delivery_place, 
            'delivery_datetime': self.delivery_datetime, 
            'gestational_age': self.gestational_age, 
            'delivery_care': self.delivery_care, 
            'delivery_via': self.delivery_via, 
            'presentation': self.presentation, 
            'birthing_events': self.birthing_events, 
            'edited_at': self.edited_at
        }