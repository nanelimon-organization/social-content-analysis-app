$(document).ready(function() {
    $.ajax({
        type: "GET",
        url: "/tweets",
        success: function(response) {
            var tweets = JSON.parse(response);
            var tweetHtml = "";
            for (var i=0; i<tweets.length; i++) {
                var tweet = tweets[i];
                tweetHtml += '<div class="col-12"><div class="container"><section class="mx-auto my-5"><div class="card"><div class="card-body"><blockquote class="blockquote blockquote-custom bg-white px-3 pt-4"><div class="blockquote-custom-icon bg-info shadow-1-strong"><i class="fa fa-quote-left text-white"></i></div><h5 class="card-title">OTHER - INOFFENSIVE</h5><p class="mb-0 mt-2 font-italic">' + tweet.content + '<a href="#" class="text-info">' + tweet.username + '</a>."</p><footer class="blockquote-footer pt-4 mt-4 border-top">' + tweet.publish_date + '<cite title="Source Title"> ' + tweet.device + '</cite> - <span title="Source Title">' + (tweet.user_location != '' ? tweet.user_location : 'Ankara, Türkiye') + '</span>';
                var hashtags = tweet.hashtags.strip('{').strip('}').split(',');
                for (var j=0; j<hashtags.length; j++) {
                    tweetHtml += '<span class="badge rounded-pill bg-warning text-dark">#' + hashtags[j].trim() + '</span>';
                }
                tweetHtml += '</footer></blockquote></div></div></section></div></div>';
            }
            $('#tweets-container').html(tweetHtml);
        }
    });
});


function updateCriterionSetNames(){
    $.ajax({
    type : "GET",
    url : "/tweets",
    data: {},
    contentType: 'application/json;charset=UTF-8',
    success: function(response) {
         for (var i=0; i<tweets.length; i++) {
                var tweet = tweets[i];
                tweetHtml += '<div class="col-12"><div class="container"><section class="mx-auto my-5"><div class="card"><div class="card-body"><blockquote class="blockquote blockquote-custom bg-white px-3 pt-4"><div class="blockquote-custom-icon bg-info shadow-1-strong"><i class="fa fa-quote-left text-white"></i></div><h5 class="card-title">OTHER - INOFFENSIVE</h5><p class="mb-0 mt-2 font-italic">' + tweet.content + '<a href="#" class="text-info">' + tweet.username + '</a>."</p><footer class="blockquote-footer pt-4 mt-4 border-top">' + tweet.publish_date + '<cite title="Source Title"> ' + tweet.device + '</cite> - <span title="Source Title">' + (tweet.user_location != '' ? tweet.user_location : 'Ankara, Türkiye') + '</span>';
                var hashtags = tweet.hashtags.strip('{').strip('}').split(',');
                for (var j=0; j<hashtags.length; j++) {
                    tweetHtml += '<span class="badge rounded-pill bg-warning text-dark">#' + hashtags[j].trim() + '</span>';
                }
                tweetHtml += '</footer></blockquote></div></div></section></div></div>';
            }
            $('#tweets-container').html(tweetHtml);
        }
    });
}