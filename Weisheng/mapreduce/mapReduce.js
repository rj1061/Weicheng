conn = new Mongo();
db = conn.getDB("weisheng");

var mapFunction = function() {
                          var key = {name:this.DBA, phone:this.PHONE, building:this.BUILDING, street:this.STREET, zip_code:this.ZIPCODE};
                          var value = { score:this.SCORE,
                                        count:1};
                          emit(key, value);
                   };

var reduceFunction = function(keySKU, countObjVals) {
                    reducedVal = { count: 0, score: 0 };

                    for (var idx = 0; idx < countObjVals.length; idx++) {
                        reducedVal.count += countObjVals[idx].count;
                        reducedVal.score += countObjVals[idx].score;
                    }

                    return reducedVal;
                 };

var finalizeFunction = function (key, reducedVal) {
                       reducedVal.avg_score = reducedVal.score/reducedVal.count;
                       return reducedVal;
                    };

db.hygiene.mapReduce( mapFunction,
                      reduceFunction,
                      {
                           out: { merge: "hygiene_average" },
                           finalize: finalizeFunction
                      }
)


