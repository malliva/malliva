import React from 'react';
import { useDispatch } from 'react-redux';
import {
  getSignUpSuccess,
  getSignUpFailure,
} from 'libs/market-app/sign-ups/src/index';

import { createAsyncThunk } from '@reduxjs/toolkit';
import axios from 'axios';

/* eslint-disable-next-line */
export interface SharedAccountSynApiProps {}

export type Error = any;

export interface SignUpState {
  first_name: string;
  last_name: string;
  username: string;
  email: string;
  password: string;
  password_confirm: string;
  market_context: string;
  user_context: string;
}

export interface SignInState {
  login: {
    email: string;
    password: string;
  };
  token: string;
  authorised: boolean;
  error: Error;
}

const API_URL = 'http://localhost:8000/';
export function SharedAccountSynApi(props: SharedAccountSynApiProps) {
  return;
}

export const postSignUpUser = createAsyncThunk(
  'malliva/register',
  async (payload: SignUpState) => {
    const formData = JSON.stringify(payload);
    let response = null;
    response = await axios.post(API_URL + 'api/v1/users/register', formData, {
      headers: { 'Content-Type': 'application/json' },
    });
    return await response.data;
  }
);

export const getSingInUser = createAsyncThunk(
  'malliva/login',
  async (payload: SignInState) => {
    const response = await fetch(
      API_URL + 'api/v1/users/login' + JSON.stringify(payload.login)
    );
    if (response.ok) {
      const serverResponse = response.json();
      return { serverResponse };
    }
    return response.json();
  }
);
