import React from 'react';

import { createAsyncThunk } from '@reduxjs/toolkit';
import axios from 'axios';

/* eslint-disable-next-line */
export interface SharedAccountSynApiProps {}

export type UserError = any;

export interface SignUpState {
  first_name: string;
  last_name: string;
  username: string;
  email: string;
  password: string;
  // password_confirm: string;
  terms_of_service_accepted: boolean;
}

export interface SignInState {
  email: string;
  password: string;
}

const API_URL = 'http://localhost:8000/';

export function SharedAccountSynApi(props: SharedAccountSynApiProps) {
  return;
}

export const postSignUpUser = createAsyncThunk(
  'malliva/register',
  async (payload: SignUpState, thunkApi) => {
    try {
      const formData = JSON.stringify(payload);
      let response = null;
      response = await axios.post(API_URL + 'api/v1/users/', formData, {
        headers: { 'Content-Type': 'application/json' },
      });
      const data = await response.data;
      return { data };
    } catch (error) {
      return thunkApi.rejectWithValue({ error: error.message });
    }
  }
);

export const getSingInUser = createAsyncThunk(
  'malliva/login',
  async (payload: SignInState, thunkApi) => {
    try {
      const formData = JSON.stringify(payload);
      const response = await axios.post(
        API_URL + 'api/v1/auth/login',
        formData,
        { headers: { 'Content-Type': 'application/json' } }
      );
      const data = await response.data;
      return { data };
    } catch (error) {
      return thunkApi.rejectWithValue({ error: error.message });
    }
  }
);

export const getRegisteredUsers = createAsyncThunk(
  'malliva/users',
  async (payload: any, thunkApi) => {
    try {
      const formData = JSON.stringify({ jwt: payload.jwt });

      let response = null;
      response = await axios.get(API_URL + 'api/v1/users/', {
        headers: { Authorization: `Bearer ${formData}` },
      });

      const data = await response.data;
      return { data };
    } catch (error) {
      return thunkApi.rejectWithValue({ error: error.message });
    }
  }
);

export const setCookieForUsersPageTheme = (key, name, value) => {
  if (key === 'edit') {
    document.cookie + '=' + value;
  }
  if (document.cookie[name] === undefined && key == 'create') {
    document.cookie = name + '=' + value;
  }
};

export const getCookieForUsersPageTheme = (name) => {
  const nameEQ = name + '=';
  const ca = document.cookie.split(';');

  for (let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') c = c.substring(1, c.length);
    if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
  }

  return null;
};
