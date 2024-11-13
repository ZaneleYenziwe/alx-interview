const request = require('request');

const movieId = process.argv[2];
const url = `(link unavailable);

request.get(url, (error, response, body) => {
    if (error) {
        console.error(error);
        return;
    }

    const data = JSON.parse(body);
    data.characters.forEach(character => {
        request.get(character, (err, res, charBody) => {
            if (err) {
                console.error(err);
                return;
            }

            const charData = JSON.parse(charBody);
            console.log(charData.name);
        });
    });
});

