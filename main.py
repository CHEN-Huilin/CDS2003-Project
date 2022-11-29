def main():
  ans=True
  while ans:
      print ("""
      ******* Phone Directory Management System *******
      1.Insert new records
      2.Delete existing records
      3.Search a record by name
      4.Display records in sorted order
      5.Quit the system
      """)
      ans=input("What would you like to do? ") 

      if ans =='1': 
        print("insert new records:")
        # Your code about how to insert new records #
      
      elif ans == '2':
        print("delete records:")
        # Your code about how to delete existing records #
      
      elif ans == '3':
        print("search a record:")      
       # Your code about how to search a record by name #

      elif ans == '4':
        print("display records in sorted order:")   
        # Your code about how to display records in sorted order#

      elif ans == '5': 
        break

      else: 
        print("Unknown Option Selected!")


if __name__ == '__main__':
    main()