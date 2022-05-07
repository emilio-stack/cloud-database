from typing import Collection
import firebase_admin                       # For firebase.
from firebase_admin import credentials      # For firebase.
from firebase_admin import firestore        # For firebase.


class Firebase_Class():
    """
    FIREBASE
        A class to work with google firebase. This class will handle
        allow for create, read, update, delete, and display functionality
    """

    def __init__(self, credential_path) -> None:
        """ 
        INIT:
            The firebase class constructor. 
            This handles all firebase initializations and connects to the database.
        Args: 
            credential_path (String): The path to the credential file.
        """
        assert isinstance(credential_path, str), "Credential path must be a string"

        _cred = credentials.Certificate(credential_path)
        firebase_admin.initialize_app(_cred)
        self._db = firestore.client()



    def _get_reference(self, collection, document = None):
        """
        GET REFERENCE:
            A method to get a reference from the database.
        Args:
            collection (String): A collection in the database to reference or 
                                 under which the document is stored.
            document (String): The document in the database to reference.
        Returns:
            ref (Reference): A reference in the database.
        """
        assert isinstance(collection, str), "Collection name must be a string"
        assert isinstance(document, str) or document == None, "Document name must be a string or none"

        if document != None:
            ref = self._db.collection(collection).document(document)
        else:
            ref = self._db.collection(collection)

        return ref



    def write(self, collection, document, data):
        """
        A method to write to the database. 
        Args: 
            collection (String): The collection in the database under which to write the data
            document (String): The document in the database under which to write the data
            data (Dict): The data to write
        """
        assert isinstance(collection, str), "Collection name must be a string"
        assert isinstance(document, str), "Document name must be a string"
        assert isinstance(data, dict), "Data must be a dictionary"
        
        self._get_reference(collection, document).set(data)



    def update(self, collection, document, field, data):
        """
        UPDATE:
            A method to update one field from the database.
        Args: 
            collection (String): The collection in the database under which the document is stored.
            document (String): The document in the database under which the field is stored.
            field (String): The field to update.
        """
        assert isinstance(collection, str), "Collection name must be a string"
        assert isinstance(document, str), "Document name must be a string"
        assert isinstance(field, str), "Field name must be a string"
        assert isinstance(data, str), "Data name must be a string"

        ref = self._get_reference(collection, document)

        # Update the field to the desired value.
        ref.update({field: data})



    def delete_field(self, collection, document, field):
        """
        DELETE FIELD:
            A method to delete one field from the database.
        Args: 
            collection (String): The collection in the database under which the document is stored.
            document (String): The document in the database under which the field is stored.
            field (String): The field to delete.
        """
        assert isinstance(collection, str), "Collection name must be a string"
        assert isinstance(document, str), "Document name must be a string"
        assert isinstance(field, str), "Field name must be a string"

        ref = self._get_reference(collection, document)

        # Update the field to the delete value.
        ref.update({field: firestore.DELETE_FIELD})



    def delete_document(self, collection, document):
        """
        DELETE DOCUMENT
            A method to delete a document in the database
        Args: 
            collection (String): The collection in the database under which the document is stored.
            document (String): The document to delete. 
        """
        assert isinstance(collection, str), "Collection name must be a string"
        assert isinstance(document, str), "Document name must be a string"

        self._get_reference(collection, document).delete()



    def delete_collection(self, collection, batch_size):
        """
        DELETE COLLECTION
            A method to delete a collection in the database
        Args: 
            collection (String): The collection in the database to delete
            batch_size (Int): How many documents to delete in the collection at a time.
        """
        assert isinstance(collection, str), "Collection name must be a string"
        assert isinstance(batch_size, int), "Batch size must be an integer"

        coll_ref = self._get_reference(collection)

        docs = coll_ref.limit(batch_size).stream()
        deleted = 0

        for doc in docs:
            print(f'Deleting doc {doc.id} => {doc.to_dict()}')
            doc.reference.delete()
            deleted = deleted + 1

        if deleted >= batch_size:
            return self.delete_collection(coll_ref, batch_size)



    def display(self, collect):
        """
        A method to display the database to the console.
        """
        docs = self._db.collection(collect).stream()

        print('\n\n\n')
        print('------------------------------------------------------------------------------------------------------------------')
        print('CURRENT DATA BASE: ')
        for doc in docs:
            print(f'{doc.id} => {doc.to_dict()}')
        print('------------------------------------------------------------------------------------------------------------------')
