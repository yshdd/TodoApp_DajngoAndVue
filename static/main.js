Vue.createApp({
    //プロパティ
    data() {
        return {
            todo:{whatTodo: ""},
            tasks: [],
        }
    },
    compilerOptions: {
        delimiters: ['[[', ']]'],
    },
    methods: {
        getTodos(){
            fetch(URL,{
                method: 'get',
                headers:{
                    'Content-Type': 'application/json',
                },
            })
            .then((response) =>{
                return response.json();
            })
            .then((todos) =>{
                this.tasks = todos;
            })
            .catch(error =>{
                console.error('There has been a problem with your fetch operation:', error);
            });
        },
        createTodo(){
            const csrftoken = Cookies.get('csrftoken');
            //todoリストの取得
            this.getTodos();
            fetch(URL_create,{
                method: 'post',
                headers:{
                    'Content-Type':  'application/json',
                    'X-CSRFToken': csrftoken,
                },
                //htmlから入力したデータをviews.pyに送信
                body:JSON.stringify(this.todo),
            })
            .then((response) =>{
                return response.json();
            })
            .then((todo) =>{
                //console.log(todo)
                this.todo.whatTodo = ''
                this.getTodos();
            })
            .catch(error =>{
                console.error('There has been a problem with your fetch operation:', error);
            });
        },
        updateFlag:function(item){
            const csrftoken = Cookies.get('csrftoken');

            let Data = {
            "todo": item.todo,
            "is_finished": item.is_finished,
            "id": item.id
            };
            
            fetch(URL_change,{
                method: 'post',
                headers:{
                    'Content-Type':  'application/json',
                    'X-CSRFToken': csrftoken,
                },
                //htmlから入力したデータをviews.pyに送信
                body: JSON.stringify(Data),
            })
            .then((response) =>{
                return response.json();
            })
            .then((todos) =>{
                //console.log(todo)
                //this.todo.whatTodo = ''
                //this.getTodos();
                this.tasks = todos;
            })
            .catch(error =>{
                console.error('There has been a problem with your fetch operation:', error);
            });
        },

        deleteTodo:function(item){
            const csrftoken = Cookies.get('csrftoken');

            let Data = {
                "id": item.id
            };
            fetch(URL_delete,{
                method: 'post',
                headers:{
                    'Content-Type':  'application/json',
                    'X-CSRFToken': csrftoken,
                },
                //htmlから入力したデータをviews.pyに送信
                body: JSON.stringify(Data),
            })
            .then((response) =>{
                return response.json();
            })
            .then((todos) =>{
                this.tasks = todos;
            })
            .catch(error =>{
                console.error('There has been a problem with your fetch operation:', error);
            });

        }
    },
    //createdとは?
    created() {
        this.getTodos();
    },
    computed:{
        doneTodo(){
            return this.tasks.filter(
                function(value){
                    return value.is_finished==true;
                }
            );
        },
        undoneTodo(){
            return this.tasks.filter(
                function(value){
                    return value.is_finished==false;
                }
            );
        },
    },

}).mount('#app')