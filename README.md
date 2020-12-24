# repositioriy_manager_ubuntu

In order for the program to be able to make changes, it must be run with administrator rights.

Requirements:
1. Each repository section to activate must be enclosed by an identification.
2. The opening ID must have the form #repo_ followed by the desired name.
3. The identification of closing the section must be the same as the opening with a "/", # / repo_

Examples of a section:

#repo_casa <br>
. <br>
deb http://####.#####.##/#### ##### #### <br>
. <br>
#/repo_casa

#repo_Hello <br>
. <br>
deb http://####.#####.##/#### ##### #### <br>
. <br>
#/repo_Hello
