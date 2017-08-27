import os, subprocess, time

def main():
    '''Backup file stored path'''
    path = "/var/Backups/"
    currentDate = time.strftime("%Y-%m-%d")
    print currentDate
    filenameOfSQL = "{0}SQL/{1}_Of_Backups.sql".format(path, currentDate)
    print "SQL Filename => %s" % (filenameOfSQL)
    filenameOfSQLGz = "%s.gz" % (filenameOfSQL)
    print "SQL Filename gz => %s" % (filenameOfSQLGz)

    subprocess.call("mysqldump --login-path=dbname BackupDB | gzip -9 > %s" % (filenameOfSQLGz), shell = True)
    filename = "{0}File/File_{1}_Backup.tar".format(path, currentDate)
    print "Filename => %s" % (filename)
    backupFile = "/File"
    subprocess.call("tar -cvpzPf %s %s" % (filename, backupFile), shell = True)

    '''Copy the backup file'''
    usbB = "B"
    cpGoalPathSQL = "/mnt/usb{0}/Linux_Server_Backup/SQL/"
    cpGoalPathFile = "/mnt/usb{0}/Linux_Server_Backup/File/"
    subprocess.call("cp %s %s" % (filenameOfSQLGz, cpGoalPathSQL.format(usbB)), shell = True)
    subprocess.call("cp %s %s" % (filename, cpGoalPathFile.format(usbB)), shell = True)

if __name__ == "__main__":
    main()