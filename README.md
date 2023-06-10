# ArrayG
ArrayG is a Python library that allows you to use numpy arrays in a similar way to regular lists in Python. This way, we save memory and make their usage easier.

## introduction

When we use `ArrayG`, we have to import it:

![Captura de pantalla 2023-06-10 123507](https://github.com/finoliso/ArrayG/assets/117580550/5c13ab6e-93e7-4e3f-8efa-8ac61e0f4f2e)

Importing only the `Arr` class is sufficient.

Now we can start creating an array in the following way.

![Captura de pantalla 2023-06-10 123634](https://github.com/finoliso/ArrayG/assets/117580550/fbb115c6-cbab-4d2e-8263-c00f86db7cc5)

In this way, what we are doing is creating and assigning the array itself to the variable `arr1`. The first parameter is the size of the array, which can be set to 0 as we can vary it in the code. The second parameter is the variable type. It is worth noting that using the string variable type can result in errors.

## add function:

Once created, we can use it in various ways. To add a value, we simply need to use the `add` function.

![Captura de pantalla 2023-06-10 123959](https://github.com/finoliso/ArrayG/assets/117580550/45c01873-cf17-49e1-bc94-06438594a99b)

In this way, it will add one more position at the end of the array, and its value will be 4.

## set_place function:

To modify the value of an already existing position, we can use the `set_place` function.

![Captura de pantalla 2023-06-10 124311](https://github.com/finoliso/ArrayG/assets/117580550/4ebb83d5-a41f-4acd-a3ad-05cd04189c8c)

The first parameter is the position of the array to be modified, and the second parameter is the new value for that position. It is crucial that the new value is of the same type as the array.

## getValue function:

If you want to know the value at a specific position in the array, you can use the `getValue` function.

![Captura de pantalla 2023-06-10 124604](https://github.com/finoliso/ArrayG/assets/117580550/bf9131e4-8094-4f6e-af8e-38c833b68f83)

We input the position we want to check, and this function will return the value located there.

## remove function:

If you want to move an element within the array, you can use the `remove` function, which will directly remove that position and replace it with another one.

![Captura de pantalla 2023-06-10 124912](https://github.com/finoliso/ArrayG/assets/117580550/4087415b-0d78-4ee2-97e4-ebf3b28b93c6)

The parameter to be entered is the position to be removed. So, for an array like [4, 2, 7, 9], removing position 2 would result in [4, 2, 9].

## set function:

Finally, the `set` function receives an input array of type NumPy and converts the entire array within the function to the new input array.

![Captura de pantalla 2023-06-10 125339](https://github.com/finoliso/ArrayG/assets/117580550/470f9a8f-7a91-4cfc-ade7-91276c3d40ad)

So, if we had an array [4, 2, 9], it would now be [6, 2, 7, 1, 5] after using the `set` function with the input array [6, 2, 7, 1, 5]. (It is obvious that in order to use NumPy, it needs to be imported beforehand.)
