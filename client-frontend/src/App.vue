<template>
    <div class="container">
        <Header @btn-click="queryDB" />
        <Orders v-if="!queryErrMsg" :orders="orders" />
        <h3 v-if="queryErrMsg">{{ queryErrMsg }}</h3>
    </div>
</template>

<script>
import axios from 'axios';
import Header from './components/Header.vue';
import Orders from './components/Orders.vue';

export default {
    name: 'App',
    components: {
        Header,
        Orders,
    },
    data() {
        return {
            orders: [],
            queryErrMsg: '',
        };
    },
    beforeMount() {
        axios
            .get('http://localhost:5000/orders')
            .then((response) => {
                console.log(response.data);
                this.orders = response.data;
                this.queryErrMsg = '';
            })
            .catch((err) => {
                this.queryErrMsg = err;
                this.orders = [];
            });
    },
    methods: {
        queryDB(URL) {
            axios
                .get(URL)
                .then((response) => {
                    console.log(response.data);
                    this.orders = response.data;
                    this.queryErrMsg = '';
                })
                .catch((err) => {
                    this.queryErrMsg = err;
                    this.orders = [];
                });
        },
    },
    created() {
        this.orders = [
            {
                order_name: 'Chrismas',
                customer_company: 'Sony Ericsson',
                customer_name: 'Dr. Harold Senger',
                order_date: 'Apr 23rd, 4:18 AM',
                delivered_amount: '$99.11',
                total_amount: '$99.11',
            },
            {
                order_name: 'Chrismas',
                customer_company: 'Comedy Central Inc',
                customer_name: 'Waylon Beahan V',
                order_date: 'Apr 23rd, 4:20 AM',
                delivered_amount: '$99.11',
                total_amount: '$99.11',
            },
        ];
    },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400&display=swap');

* {
    font-family: 'Poppins';
}

.container {
    padding-left: 20px;
    padding-right: 20px;
}
</style>
