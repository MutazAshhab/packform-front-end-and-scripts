<template>
    <div>
        <header>
            <IconedButton
                id="search_button"
                @click="search"
                text="Search"
                icon="fa-search"
            />
            <input
                id="search"
                type="text"
                v-model="search_text"
                name="search_text"
                placeholder="Search..."
            />
        </header>
        <h4>Created Date</h4>
        <span>Start Date: </span>
        <input
            class="date_input"
            type="date"
            v-model="start_date"
            name="start_date"
            placeholder="Start Date"
        />
        <span class="tab">End Date: </span>
        <input
            class="date_input"
            type="date"
            v-model="end_date"
            name="end_date"
            placeholder="End Date"
        />
        <h4 class="total_amount">
            Total amount:
            <span class="total_amount_value">${{ total_amount }}</span>
        </h4>
    </div>
</template>

<script>
import IconedButton from './IconedButton.vue';

export default {
    name: 'Header',
    data() {
        return {
            search_text: '',
            start_date: '',
            end_date: '',
        };
    },
    props: {},
    components: {
        IconedButton,
    },
    methods: {
        search() {
            URL = 'http://localhost:5000/orders';
            if (
                this.search_text === '' &&
                this.start_date === '' &&
                this.end_date === ''
            ) {
                this.$emit('btn-click', URL);

                this.search_text == '';
                this.start_date == '';
                this.end_date == '';
                return;
            }

            // TODO: Fix URL for searched items.
            // URL = URL + ''
            this.$emit('btn-click', URL);
            this.search_text == '';
            this.start_date == '';
            this.end_date == '';
        },
    },
    emits: ['btn-click'],
};
</script>

<style scoped>
header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}
#search {
    width: 92%;
}
.date_input,
#search_button,
#search {
    padding: 8px;
}
.total_amount {
    font-weight: initial;
}
.total_amount_value {
    font-weight: bold;
}
.tab {
    margin-left: 2.5em;
}
</style>
