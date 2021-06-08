import { createSlice, Action, PayloadAction } from 'redux-starter-kit';
import { createSelector } from 'reselect';
import { ThunkAction } from 'redux-thunk';

export const USERS_KEY = 'users';

export type UsersError = any;

export interface UsersState {
  username: string;
  authorised: boolean;
  error: UsersError;
}

export const initialUsersState: UsersState = {
  username: '',
  authorised: false,
  error: null,
};
