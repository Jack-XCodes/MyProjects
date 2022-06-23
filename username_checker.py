#checks new username if already available in the current user

current_users=['Derick','Rickfargason', 'Maritn' ,'Rickardo']

new_users=['Derick','Micky','Carlos','maritin']

for new_user in new_users:
    if new_user in current_users:
        print(f'Sorry, the name {new_user}  is already taken try again')

    else:
        print(f'Nice name {new_user} .You have now created the account succesfully!')