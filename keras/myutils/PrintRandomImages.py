def PrintRandomImages(X,y,numItr,seed=0):
    random.seed(seed)
    for _ in range(0,numItr):
        randImage = random.randint(0,len(X))
        plt.imshow(X[randImage])
        plt.show()
        plt.imshow(y[randImage])
        plt.show()