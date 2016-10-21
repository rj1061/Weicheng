conn = new Mongo();
db = conn.getDB("weisheng");
db.yelpDataMain.find().forEach(
  function(e) {
    e.name = e.name.toUpperCase();
    db.yelpDataMain.save(e);
  }
);
db.hygiene.aggregate([
        {
                $lookup:
                {
                        from:"yelpDataMain",
                        localField:"DBA",
                        foreignField:"name",
                        as:"yelp"
                }
        },
        {       $out:"yelp_hygiene"}
]);

