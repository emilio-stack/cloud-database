import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.Certificate("/Users/Emilio_1/Documents/CSE/CSE310/cloud-database/hello-world-2ad04-firebase-adminsdk-vebcn-945b8b0773.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


##############################################################
# CREATE DATA
##############################################################
data = {
    u'name': u'Los Angeles',
    u'state': u'CA',
    u'country': u'USA'
}

more_data = {
    u'name': u'Charlotte',
    u'state': u'NC',
    u'country': u'USA'
}

even_more_data = {
    u'name': u'Flexburg',
    u'state': u'ID',
    u'country': u'USA'
}

person = {
    u'first' : u'Tim',
    u'last' : u'Tam',
    u'age' : u'23'
}

another_person = {
    u'first' : u'Beth',
    u'last' : u'Bradey',
    u'age' : u'33'
}

yet_another_person = {
    u'first' : u'Sue',
    u'last' : u'Silvester',
    u'age' : u'66'
}

# Add a new doc in collection 'cities' with ID 'LA'
# db.collection(u'cities').document(u'LA').set(data)
# db.collection(u'cities').document(u'CLT').set(more_data)
# db.collection(u'cities').document(u'FX').set(even_more_data)
db.collection(u'people').document(u'person').set(person)
db.collection(u'people').document(u'another_person').set(another_person)
db.collection(u'people').document(u'yet_another_person').set(yet_another_person)

##############################################################
# DELETE DATA
##############################################################
# db.collection(u'cities').document(u'LA').delete()

def delete_collection(coll_ref, batch_size):
    docs = coll_ref.limit(batch_size).stream()
    deleted = 0

    for doc in docs:
        print(f'Deleting doc {doc.id} => {doc.to_dict()}')
        doc.reference.delete()
        deleted = deleted + 1

    if deleted >= batch_size:
        return delete_collection(coll_ref, batch_size)

# delete_collection(db.collection(u'cities'), 10)

##############################################################
# READ DATA
##############################################################
# doc_ref = db.collection(u'cities').document(u'LA')

# doc = doc_ref.get()
# if doc.exists:
#     print(f'Document data: {doc.to_dict()}')
# else:
#     print(u'No such document!')

##############################################################
# UPDATE DATA
##############################################################
# city_ref = db.collection(u'cities').document(u'LA')
# city_ref.update({
#     u'state': firestore.DELETE_FIELD # Or change value here
# })