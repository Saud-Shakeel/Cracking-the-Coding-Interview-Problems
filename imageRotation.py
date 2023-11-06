# def imageRotation(img):
#     n = len(img)
#     new_img = [[0]*n for pic in range(n)]

#     print("Original Image: ")
#     for x in img:
#         print(x)
#     print('\n')

#     for col in range(len(img)):
#         for row in range(len(img)-1,-1,-1):
#             new_img[col][abs(row-2)] = img[row][col]

#     print('After 90 Degree Rotation:')
#     for row in new_img:
#         print(row)


# imageRotation([[1,2,3],[4,5,6],[7,8,9]])

def imageRotation(img):
    n = len(img)

    print('Original Image:')
    for x in img:
        print(x)
    print('\n')

    for row in range(n):
        for col in range(row, n):
            img[row][col], img[col][row] = img[col][row], img[row][col]

    print('After 90 Degree Rotation:')
    for i in img:
        i.reverse()
        print(i)

imageRotation([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
