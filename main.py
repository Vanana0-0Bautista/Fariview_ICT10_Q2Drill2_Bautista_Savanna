from pyscript import document, display

#the original list of club members
club_members = [
    "Seana Bautista",
    "Carlos Borromeo",
    "Jericho Magsalin", 
    "Anya Basuil",
    "Orange Mendoza",
    "Anderdingus Bert",
    "Chloe Crest",
    "Maybelline Marquez",
    "Dogo Mark",
    "Marvin Hetro"
    ]

club_members.append(full_name)


#the function that will be called when you submit the names
def submit_form(e):

    first_name = document.getElementById("first_name").value

    last_name = document.getElementById("last_name").value

    full_name = first_name + " " + last_name

    members_list = "<br>".join(sorted(club_members))

    document.getElementById("result").innerHTML = f"<h3>Club Members:</h3><p>{members_list}</p>"