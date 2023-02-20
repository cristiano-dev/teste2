Import("env")

print("#####################")
print("Deu certo")
print("#####################")

host = env.GetProjectOption("custom_ping_host")

print( "Host: " + host )
