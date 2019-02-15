# MinesSweeper
MinesSweeper adaptation in a Model-View-Controller patron. TKinter library is use to adapt the view.
The main class is used to launch the program.There you can select the rows and the columns of the game. Eventhought when you are playing you just can select 3 kinds of board.
There is an observer interface and an observable(with a list of observers) class for the view and the model respectively. Any change in the model(the observable) is notify to the view by the notifyall method.
In this patron there can be many views which must be registered at the model to receive the notifications.

