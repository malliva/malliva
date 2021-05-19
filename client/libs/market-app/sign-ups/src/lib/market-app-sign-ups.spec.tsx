import { render } from '@testing-library/react';

import MarketAppSignUps from './market-app-sign-ups';

describe('MarketAppSignUps', () => {
  it('should render successfully', () => {
    const { baseElement } = render(<MarketAppSignUps />);
    expect(baseElement).toBeTruthy();
  });
});
