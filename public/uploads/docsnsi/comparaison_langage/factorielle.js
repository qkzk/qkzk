const factorielle = 
          n => {
                  if ( n === 0) 
                    return 1;
                  else if ( n === 1) 	
                    return 1;
                  else {
                    let result = 1;
                    let i = 0;
                    while (i < n) {
                      i = i + 1;
                      result = result * i;
                    }
                    return result;
                  }
              }
