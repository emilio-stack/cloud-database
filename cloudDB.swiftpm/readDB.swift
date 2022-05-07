//
//  File.swift
//  cloudDB
//
//  Created by Emilio on 5/3/22.
//

import Firebase

class FirebaseClass {
   
   //   Singleton pattern
   static let shared = FirebaseClass()
   var database: Firestore? = nil
   
   // The class
   init() {
      FirebaseApp.configure()
      database = Firestore.firestore()
   }
   
   // Get the entire database
   func getData() {
      
   }
   
   // Write to the database
   func writeData() {
      
   }
}
