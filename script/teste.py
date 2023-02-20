Import("env")

print("#####################")
print("Deu certo")
print("version: 1.0.0")
print("#####################")

DIR = env.subst("$PROJECT_DIR")
print( "DIR: " + DIR )
