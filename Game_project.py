{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "8463df2e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Select\n",
      " 1 for Rock\n",
      " 2 for paper \n",
      " 3 for scissor\n",
      "Select a value: 3\n",
      "Do you want to continue? Y or N : Y\n",
      "Select a value: 3\n",
      "Draw\n",
      "Do you want to continue? Y or N : Y\n",
      "Select a value: 2\n",
      "Draw\n",
      "Do you want to continue? Y or N : Y\n",
      "Select a value: 1\n",
      "Draw\n",
      "Do you want to continue? Y or N : Y\n",
      "Select a value: 2\n",
      "Draw\n",
      "Do you want to continue? Y or N : Y\n",
      "Select a value: 3\n",
      "Draw\n",
      "Do you want to continue? Y or N : Y\n",
      "Select a value: 3\n",
      "Draw\n",
      "Do you want to continue? Y or N : Y\n",
      "Select a value: 1\n",
      "Do you want to continue? Y or N : Y\n",
      "Select a value: 3\n",
      "Do you want to continue? Y or N : Y\n",
      "Select a value: 2\n",
      "Do you want to continue? Y or N : Y\n",
      "Select a value: 3\n",
      "Do you want to continue? Y or N : Y\n",
      "Select a value: 2\n",
      "Draw\n",
      "Do you want to continue? Y or N : N\n",
      "*Score*\n",
      " computer --> 3 \n",
      " your --> 2\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "option1=['Rock','Paper','Scissor']\n",
    "option2={1:'Rock',2:'Paper',3:'Scissor'}\n",
    "print('Select\\n 1 for Rock\\n 2 for paper \\n 3 for scissor')\n",
    "    \n",
    "c=0\n",
    "\n",
    "u=0\n",
    "\n",
    "\n",
    "\n",
    "def Game(computer,user):\n",
    "    global c\n",
    "    global u\n",
    "    if(computer==user):\n",
    "        print('Draw')\n",
    "    elif(computer=='Rock' and user=='Paper'):\n",
    "        u+=1\n",
    "    elif(computer=='Paper' and user=='Scissor'):  \n",
    "        u+=1\n",
    "    elif(computer=='Scissor' and user=='Rock'):\n",
    "        u+=1\n",
    "    elif(computer=='Paper' and user=='Rock'):\n",
    "        c+=1\n",
    "    elif(computer=='Scissor' and user=='Paper'):\n",
    "        c+=1\n",
    "    elif(computer=='Rock' and user=='Scissor'):\n",
    "        c+=1\n",
    "        \n",
    "while(1):\n",
    "    a=int(input('Select a value: '))\n",
    "    user=option2[a]\n",
    "    computer=random.choice(option1)\n",
    "    Game(computer,user)\n",
    "    ch=input('Do you want to continue? Y or N : ')\n",
    "    if(ch=='N'):\n",
    "        print('*Score*\\n computer -->',c,'\\n your -->',u)\n",
    "        break\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d0004291",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a338c6cc",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
