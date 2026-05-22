# Design Pattern
## Factory pattern
There are 3 factory classes defined AnimalFactory, DogFactory and CatFactory. all implemented create_product interface defined in abstract Factory class.
Dog and Cat classes implemented run interface defined in Animals abstract class.
Dog instance can be created by DogFactory with create_product() method so client can create dog instance without knowning the details how the dog is instantiated.
