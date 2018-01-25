class RetrieveVendorMetaData:
    @staticmethod
    def get_vendor_data():
        return [
            {
                "vendor": "GlassByte Barbers",
                "meta": {
                    "target_gender": "male",
                    "logo": "http://www.glassbyte.com/images/logo.png",
                    "location": {
                        "lat": 53.359755,
                        "lng": -6.261555
                    },
                    "tags": [
                        "dry", "student"
                    ]
                },
                "opening_hours": {
                    "monday": {"opening": "9:00", "closing": "19:00"},
                    "tuesday": {"opening": "9:00", "closing": "19:00"},
                    "wednesday": {"opening": "9:00", "closing": "19:00"},
                    "thursday": {"opening": "9:00", "closing": "20:00"},
                    "friday": {"opening": "9:00", "closing": "20:00"},
                    "saturday": {"opening": "9:00", "closing": "18:00"},
                    "sunday": {"opening": "9:00", "closing": "18:00"},
                },
                "prices": {
                    "Wet Cut": 15,
                    "Dry Cut": 10,
                    "Beard Trim": 7,
                    "Student Deal": 8,
                    "Children": 7
                },
                "barbers": [
                    {
                        "forename": "Edmond",
                        "surname": "Ó Floinn",
                        "ig_username": "earwax_man"
                    },
                    {
                        "forename": "Alexandru",
                        "surname": "Sulea",
                        "ig_username": "alexsulea"
                    }
                ]
            }
        ]
