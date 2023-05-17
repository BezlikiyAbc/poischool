class API {
    constructor(baseUrl) {
        this.baseUrl = baseUrl;
    }

    getData = async (path) => {
        try {
            const { data } = await axios.get(`${this.baseUrl}${path}`);
            return data;
        }   catch (errors) {
            console.error(errors);
        }
    };
}

const dashaApi = new API("http://127.0.0.1:8000/");

const getUsers = async () => {
    axios.get(`http://127.0.0.1:8000/schoolAll/`, 
    {headers: {'token': 'admin'}});
}

const main = async () => { 
    await console.log(getUsers())
}

main()