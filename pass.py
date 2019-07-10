import os, sys
'clear'
print ("\033[1;32mSILAHKAN MASUKAN USERNAME DAN PASSwORD NYA")
print ("\033[1;32mKALAU TIDAK TAU SILAHKAN HUBUNGI FIQRA ID")
print ("\033[1;36mFB : FIQRA ID")
print ("\033[1;36mTTD : FIQRA THANVANS")
username = 'GASPOLL'
password = 'MANTUL'

def restart():
        ngulang = sys.executable
        os.execl(ngulang, ngulang, *sys.argv)

def main():
        uname = raw_input("username : ")
        if uname == username:
                pwd = raw_input("password : ")
                if pwd == password:
                        print "\n\033[1;34mSELAMAT DATANG DI TOOLS FIQRA ID",
                        sys.exit()

                else:
                        print "\n\033[1;36mmaaf password yg anda masukan salah !!!\033[00m"
                        print "log-in kembali\n"
                        restart()

        else:
                print "\n\033[1;36mmaaf username yg anda masukan salah !!!\033[00m"
                print "log-in kembali\n"
                restart()

try:
        main()
except KeyboardInterrupt:
       os.system('clear')
       restart()
