import os
import pydicom
 
def get_file_list(dir) :
    try :
        list_full = []
        for (path, _, file) in os.walk(dir):
            for each_file in file:
                if each_file[-3:] == 'dcm' or each_file[-5:] == "dicom":
                    list_full.append(os.path.join(os.getcwd(),path,each_file))
        return list_full
    except : 
        return 'get_file_list error.'    
 
def de_identifier(filename):
    try:
        Metadata = pydicom.filereader.dcmread(str(filename))
    except: return 'de_identifier // file reading error. '
    try:
        # de-identify
        Metadata.PatientName = 'Anonymized'
        Metadata.PatientBirthDate = 'Anonymized'
        Metadata.PatientSex = 'Anonymized'
        Metadata.OtherPatientIDs = 'Anonymized'
        Metadata.PatientAge = 'Anonymized'
        Metadata.RequestingPhysician = 'Anonymized'
        Metadata.InstitutionName = 'Anonymized'
        Metadata.InstitutionAddress = 'Anonymized'
        Metadata.ReferringPhysicianName = 'Anonymized'
        Metadata.StationName = 'Anonymized'
        Metadata.PhysiciansofRecord = 'Anonymized'
 
        Metadata.save_as(str(filename))
 
    except:            
            return 'de_identifier error'

if __name__ == "__main__":
    
    while True:
        dir_path = input("Enter the directory path: ")
        if os.path.exists(dir_path):
            break
        else:
            print("Invalid path")

    dcm_list = get_file_list(dir_path)
    
    for filename in dcm_list:
        de_identifier(filename)