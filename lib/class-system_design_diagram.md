   Nouns:                                   Verbs:
      Customer                                 check
      list of dishes with prices               order something/meal I want
      meal                                     select several available dishes
      Receipt                                  Verify order is correct
      Grand Total

   ┌────────────────────┐                                  ┌─────────────────────┐
   │  Customer Order()  │◄─────────────────────────────────┤ Restaurant Class    │
   │ - order_items      │                                  │ - dict_of_dishes w/ │
   │    {meal:price}    │                                  │   prices{}          │
   │ - restaurant       │                                  │                     │
   │ - customer_name    │    ┌────────────────────┐        │ - get_menu()        │
   │                    │    │  Meal Class        │        │                     │
   │ - get_receipt()    │    │                    │        │ - add_meal()        │
   │                    │    │ -self.meal         │        │                     │
   │ - order_takeaway() │    │ -self.price        ├───────►│                     │
   └────────────────────┘    │ -self.info{}       │        └─────────────────────┘
                           │                    │
                           │                    │
                           │                    │
                           │                    │
                           └────────────────────┘
