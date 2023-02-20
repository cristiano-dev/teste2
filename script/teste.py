Import("env")

print("#####################")
print("Deu certo")
print("version: 0.0.0")
print("#####################")

DIR = env.subst("$PROJECT_DIR")
print( "DIR: " + DIR )
