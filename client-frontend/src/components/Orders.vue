<template>
    <table>
        <tr>
            <td class="header">Order Name</td>
            <td class="header">Cusomter Company</td>
            <td class="header">Customer Name</td>
            <td class="header">Order Date</td>
            <td class="header">Delivered Amount</td>
            <td class="header">Total Amount</td>
        </tr>
        <tr :key="order.order_name" v-for="order in orders">
            <Order :order="order" />
        </tr>
    </table>
</template>

<script>
import Order from './Order.vue';

export default {
    name: 'Orders',
    props: {
        orders: Array,
    },
    components: {
        Order,
    },
};
</script>

<style scoped>
table {
    width: 100%;
}
.header {
    color: grey;
    font-weight: bold;
}
</style>
