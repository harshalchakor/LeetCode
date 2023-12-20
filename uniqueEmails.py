
class Answer:
    def uniqueEmails(self, emails) -> int:
        
        unique = set()
        
        for email in emails:
            local, domain = email.split("@")     # xy.z+full@gmail.com  --->  xy.z+full
            local = local.split("+")[0]          # xy.z+full            --->  xy.z
            local = local.replace(".","")        # xy.z                 --->  xyz
        
            unique.add((local + "@" + domain))
        
        print(unique)
        
        return len(unique)
        
        #-----------------Second Method---------------------------#
        
        for email in emails:
            i = 0
            local = ""
            while email[i] not in ["@","+"]:
                if email[i] != ".":
                    local += email[i]
                i += 1
            
            domain = ""
            while email[i] != "@":
                i += 1
            domain = email[i+1:]
            
            unique.add((local + "@" + domain))
            
        print(unique)
        return len(unique)
            
                    
ans = Answer()
# here false means Prime number or True means not a prime number
print(ans.uniqueEmails(["x.yz@gmail.com", "xyz+name@gmail.com", "xy.z+full@gmail.com", 
                    "nitin@hotmail.com", "yz+x@gmail.com"]))
