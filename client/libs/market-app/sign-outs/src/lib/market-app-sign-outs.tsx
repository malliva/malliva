import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import {
  getCookieForUsers,
  postSingOutUser,
  setCookieForUsers,
} from '@client/shared/account-syn-api';

import './market-app-sign-outs.module.scss';
import { selectSignOutStateStateLoaded } from './market-app-sign-outs.slice';

/* eslint-disable-next-line */
export interface MarketAppSignOutsProps {}

export function MarketAppSignOuts(props: MarketAppSignOutsProps) {
  const dispatch = useDispatch();
  const { response, loading } = useSelector(selectSignOutStateStateLoaded);

  if (loading === 'succeeded') {
    setCookieForUsers('create', 'jwt', '');
  }

  useEffect(() => {
    dispatch(postSingOutUser());
  }, [dispatch]);

  return (
    <div className="text-center">
      <h1>Welcome to market-app-sign-outs!</h1>
    </div>
  );
}

export default MarketAppSignOuts;
