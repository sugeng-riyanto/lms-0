
# Getting Started with C++

### Requirements before you start

-   To start using C++, you need two things:
    

    -   A text editor, like Notepad, or an IDE, like VSCode to act as a platform for you to write C++ code
        
    -   A compiler, like GCC to translate the C++ code you have written which is a high-level language into a low-level language that the computer will understand.
        

### What is an IDE?

-   IDE stands for Integrated Development Environment.
    
-   It is nothing more than an enhanced version of a text editor that helps you write more efficient and nicer code.
    
-   It helps to differentiate different parts of your codes with different colors and notifies you if you are missing some semicolon or bracket at some place by highlighting that area.
    
-   A lot of IDEs are available, such as DEVC++ or Code Blocks, but we will prefer using VS Code for this tutorial series.
    

### Installing VSCode

-   Visit  [https://code.visualstudio.com/download](https://code.visualstudio.com/download)
    
-   Click on the download option as per your operating system.
    
-   After the download is completed, open the setup and run it by saving VS Code in the default location without changing any settings.
    
-   You will need to click the next button again and again until the installation process begins.
    

### What is a Compiler?

-   A compiler is used to run the program of a certain language which is generally high-level by converting the code into a language that is low-level that our computer could understand.
    
-   There are a lot of compilers available, but we will proceed with teaching you to use MinGW for this course because it will fulfill all of our requirements, and also it is recommended by Microsoft itself.
    

### Setting up the compiler

-   Visit  [https://code.visualstudio.com/docs/languages/cpp](https://code.visualstudio.com/docs/languages/cpp)
    
-   Select C++ from the sidebar.
    
-   Choose “GCC via Mingw-w64 on Windows” from the options shown there.
    
-   Select the install sourceforge option.
    
-   After the downloading gets completed, run the setup and choose all the default options as we did while installing VS Code.
    

### Setting Path for Compiler

-   Go to the C directory. Navigate into the Program Files. Then, open MinGW-64. Open MinGW-32. And then the bin folder. After reaching the bin, save the path or URL to the bin.
    
-   Then go to the properties of ‘This PC’.
    
-   Select ‘Advance System Settings’.
    
-   Select the ‘Environment Variable’ option.
    
-   Add the copied path to the Environment Variable.
    
-   And now, you can visit your IDE and run your C++ programs on it. The configuration part is done.
    

### Writing your first code in C++

Open VSCode. Here’s the simplest print statement we can start with.

```cpp
#include <iostream>
 
int main()
{
    std::cout << "Hello World";
    return 0;
}

```


**Output:**

```cpp
Hello World
```