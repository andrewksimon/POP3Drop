# This script had been written by Andrew Simon.
# This scrip was written on 09/06/2018
# The purpose of this script is to delete messages on a POP3 server (especially if they are in large quantities).

# Import statements
import poplib # POP3 Manipulation library

# Defines environment variables
user = 'user' # Inbox username - user@domain.com
passw = 'password' # Inbox user's password
pop3hst = 'domain.com' # POP3 hostname/resolver
port = '110' # POP3 Port number... ~ NON SSL

# Sets up the connection
Mailbox = poplib.POP3(pop3hst, port) # Define the instance "Mailbox" with the connection
Mailbox.user(user) # Defines the mailbox's connection username.
Mailbox.pass_(passw) # Defines the mailbox's connection password.
numMessages = len(Mailbox.list()[1]) # Grabs the total number of emails that are sitting on user's account.
print(Mailbox.getwelcome()) # Gets welcome message - usual Dovecot server greeting
print("Total messages: " + str(numMessages) + "\n") # Print out total number of messages on the server.

# Iterate through from message #1 to total number of messages that are on the server.
# IMPORTANT: i must start at 1... 0 is not a message index.
for i in range(1, numMessages+1):
    print("Deleting Message #" + str(i) + "...") # Verbose message.
    Mailbox.dele(i) # POP3 delete command.
    print("DELETED Message #" + str(i)) # Verbose message.
    print("There are now " + str(len(Mailbox.list()[1])) + " messages left. \n") # Verbose message... reprint # of msgs.

print("Committing changes to server... this may take a while...")
newMsgLst = str(len(Mailbox.list()[1]))
Mailbox.quit() # Close the connection to the machine.
print("CHANGES COMITTED! There is " + newMsgLst + " message(s) left on the server.")
print("Connection to " + user + "@" + pop3hst + " has now been close. Have a good day!")
