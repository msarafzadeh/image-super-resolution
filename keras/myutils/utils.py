
#todo CREATE FUNCTION TO READ AN IMAGE WITH A GENERATOR AND PREPROCESS THEM FOR THE NEURAL NETWORK (INSTEAD OF SAVING ALL TO MEMORY)


def CheckKerasGpu():
    #making sure GPU is in use 
    from tensorflow.python.client import device_lib
    print(device_lib.list_local_devices())
    
    
def PrintRandomImages(X,y,numItr,seed=0):
    random.seed(seed)
    for _ in range(0,numItr):
        randImage = random.randint(0,len(X))
        plt.imshow(X[randImage])
        plt.show()
        plt.imshow(y[randImage])
        plt.show()