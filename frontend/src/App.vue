<template>
    <div id="app">
        <b-navbar class="custom-container" toggleable="lg" type="dark">
            <router-link tag="b-navbar-brand" to="/">STORMWIND</router-link>
            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
            <b-collapse id="nav-collapse" is-nav="">
                <b-navbar-nav>
                    <router-link class="a" tag="b-nav-item" :to="'/Offers'">Offers</router-link>
                    <router-link class="a" tag="b-nav-item" :to="'/Requirements'">Requirements</router-link>
                </b-navbar-nav>
                <b-navbar-nav class="ml-auto">
                    <b-nav-item-dropdown right="">
                        <template ñlass="a" #button-content="">
                           User
                        </template>
                        <router-link tag="b-dropdown-item" :to="'/Registration'">Sign up</router-link>
                        <router-link tag="b-dropdown-item" :to="'/Enterance'">Sign in</router-link>
                    </b-nav-item-dropdown>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
        <b-container>
            <router-view />
        </b-container>
    </div>
</template>
<script>
</script>

<style>
</style>
