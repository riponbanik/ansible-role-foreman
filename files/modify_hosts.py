import re, sys

def replace(file, ipaddr, ipaddr_fqdn_hostname):
  file_handle = open(file, 'r')
  file_string = file_handle.read()
  file_handle.close()
  #print("Before modification" + file_string)
  pattern = re.compile('%s\s*(\w*)' % ipaddr)
  #print("Pattern to replace" + str(pattern))
  file_string = (re.sub(pattern, ipaddr_fqdn_hostname, file_string))
  file_handle = open(file, 'w')  
  file_handle.write(file_string)
  #print("After modification" + file_string)
  file_handle.close()

if __name__ == "__main__":
  if len(sys.argv) < 3:
    sys.stderr.write("Usage: %s ip_address \"ip_address fqdn hostname\"\n" % (sys.argv[0]))
    exit()
  replace("/etc/hosts", sys.argv[1], sys.argv[2])