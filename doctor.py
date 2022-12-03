class Doctor:
    doctorObject_List = []

    def __init__(self, id="", name="", specialization="", workingTime="", qualification="", roomNumber=""):
        self.id = id
        self.name = name
        self.specialization = specialization
        self.workingTime = workingTime
        self.qualification = qualification
        self.roomNumber = roomNumber

    def enterDrInfor(self):
        id = input("Enter the doctor’s ID:")
        name = input("Enter the doctor’s name:")
        specialization = input("Enter the doctor’s specility:")
        workingTime = input("Enter the doctor’s timing (e.g., 7am-10pm):")
        qualificaiton = input("Enter the doctor’s qualification:")
        roomNumber = input("Enter the doctor’s room number:")
        return id, name, specialization, workingTime, qualificaiton, roomNumber

    def readDoctorsFile(self):
        f = open("doctors.txt", "r")
        lines = f.readlines()
        for line in lines:
            doc = line.split("_")
            doctorObject = Doctor(
                doc[0], doc[1], doc[2], doc[3], doc[4], doc[5])
            self.doctorObject_List.append(doctorObject)

    def displayDoctorsList(self):
        for i in range(len(self.doctorObject_List)):
            doctor = self.doctorObject_List[i]
            print("{:20} {:20} {:20} {:20} {:20} {:20}".format(doctor.id, doctor.name,
                  doctor.specialization, doctor.workingTime, doctor.qualification, doctor.roomNumber))

    def searchDoctorById(self):
        userInputId = input("Enter the doctor Id: ")

        for doctor in self.doctorObject_List:
            if userInputId == doctor.id:
                print("{:20} {:20} {:20} {:20} {:20} {:20}".format(self.doctorObject_List[0].id, self.doctorObject_List[0].name,  self.doctorObject_List[
                    0].specialization, self.doctorObject_List[0].workingTime, self.doctorObject_List[0].qualification, self.doctorObject_List[0].roomNumber))
                print("{:20} {:20} {:20} {:20} {:20} {:20}".format(doctor.id, doctor.name, doctor.specialization, doctor.workingTime, doctor.qualification, doctor.roomNumber
                                                                   ))
                return
        print("Can't find the doctor with the same ID on the system")

    def formatDrInfo(self):
        # return f"{id}+_+{name}"
        pass

    def addDrToFile(self):
        # open file for writing
        # ask for facility info
        # format the info in the right way for the file
        # then write into the file
        pass


# Doctor().enterDrInfor()
Doctor().readDoctorsFile()
Doctor().displayDoctorsList()
Doctor().searchDoctorById()
