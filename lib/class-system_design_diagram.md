Nouns:                                   Verbs:
   Customer                                 check
   list of dishes with prices               order something/meal I want
   meal                                     select several available dishes
   Receipt                                  Verify order is correct
   Grand Total



┌────────────────────┐                                  ┌─────────────────────┐
│  Customer Class    │◄─────────────────────────────────┤ Restaurant Class    │
│ - orders           │                                  │ - dict_of_dishes w/ │
│ {restaurant:total} |                                  │   prices[]          │
│                    │                                  │                     │
│ - get_receipt()    │    ┌────────────────────┐        │ - get_menu()        │
│                    │    │  Meal Class        │        │                     │
│                    │    │                    │        │                     │ 
│                    │    │ -self.meal         │        │                     │
│                    │    │ -self.price        ├───────►│ - add_meal()        │
└────────────────────┘    │                    │        └─────────────────────┘
         ▲                │                    │                   ▲
         │                │                    │                   │
         │                │                    │                   │
         │                │                    │                   │
         │                └────────────────────┘                   │
         │                                                         │
         │                                                         │
         │                                                         │
     ┌───┴────────────────────┐                                    │
     │  Order Class           │                                    │
     │                        │                                    │
     │ - place_order()        │                                    │
     │   Parameters: customer,│                                    │
     │   meals, restaurant    ├────────────────────────────────────┘
     │                        │
     │                        │
     │                        │
     │                        │
     │                        │
     └────────────────────────┘


