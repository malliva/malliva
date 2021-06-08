import React from 'react';

import { createAsyncThunk } from '@reduxjs/toolkit';

/* eslint-disable-next-line */
export interface SharedAccountSynApiProps {}
export interface registerUser {
  first_name: string;
  last_name: string;
  username: string;
  email: string;
  password: string;
}

export interface loginUser {
  email: string;
  password: string;
}
const API_URL = 'http://localhost:5000/';

export function SharedAccountSynApi(props: SharedAccountSynApiProps) {
  return;
}

export function registerUser(registerUser) {
  createAsyncThunk('malliva/register', async () => {
    const response = await fetch(
      API_URL + 'api/v1/user/register' + registerUser
    );
    if (response.ok) {
      const serverResponse = response.json();
      return { serverResponse };
    }
  });
}

export function loginUser(loginUser) {
  createAsyncThunk('malliva/login', async () => {
    const response = await fetch(API_URL + 'api/v1/user/login' + loginUser);
    if (response.ok) {
      const serverResponse = response.json();
      return { serverResponse };
    }
  });
}
